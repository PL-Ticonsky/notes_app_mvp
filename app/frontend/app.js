const API_BASE = "http://127.0.0.1:8000";

const els = {
  apiBase: document.getElementById("apiBase"),
  listMsg: document.getElementById("listMsg"),
  notesList: document.getElementById("notesList"),
  refreshBtn: document.getElementById("refreshBtn"),

  form: document.getElementById("noteForm"),
  formMsg: document.getElementById("formMsg"),
  noteId: document.getElementById("noteId"),
  title: document.getElementById("title"),
  content: document.getElementById("content"),
  saveBtn: document.getElementById("saveBtn"),
  cancelBtn: document.getElementById("cancelBtn"),
};

els.apiBase.textContent = API_BASE;

function setMsg(el, msg, isError = false) {
  el.textContent = msg || "";
  el.style.color = isError ? "var(--danger)" : "";
}

function escapeHtml(s) {
  return s
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

async function api(path, options = {}) {
  const res = await fetch(`${API_BASE}${path}`, {
    headers: { "Content-Type": "application/json", ...(options.headers || {}) },
    ...options,
  });

  // FastAPI returns 204 for delete, with no json
  if (res.status === 204) return { ok: true, status: 204, data: null };

  let data = null;
  const text = await res.text();
  try { data = text ? JSON.parse(text) : null; } catch { data = text; }

  if (!res.ok) {
    const err = new Error(`HTTP ${res.status}`);
    err.status = res.status;
    err.data = data;
    throw err;
  }
  return { ok: true, status: res.status, data };
}

function resetForm() {
  els.noteId.value = "";
  els.title.value = "";
  els.content.value = "";
  els.saveBtn.textContent = "Save";
  els.cancelBtn.hidden = true;
  setMsg(els.formMsg, "");
}

function fillForm(note) {
  els.noteId.value = note.id;
  els.title.value = note.title ?? "";
  els.content.value = note.content ?? "";
  els.saveBtn.textContent = "Update";
  els.cancelBtn.hidden = false;
  setMsg(els.formMsg, `Editing: ${note.id}`);
}

function renderNotes(notes) {
  els.notesList.innerHTML = "";

  for (const n of notes) {
    const li = document.createElement("li");
    li.className = "note";

    li.innerHTML = `
      <div class="meta">
        <h3>${escapeHtml(n.title || "(no title)")}</h3>
        <span class="badge">${new Date(n.updated_at).toLocaleString()}</span>
      </div>
      <p>${escapeHtml(n.content || "")}</p>
      <div class="actions">
        <button data-action="edit">Edit</button>
        <button data-action="delete" class="danger">Delete</button>
      </div>
    `;

    li.querySelector('[data-action="edit"]').addEventListener("click", () => fillForm(n));
    li.querySelector('[data-action="delete"]').addEventListener("click", async () => {
      const ok = confirm(`Delete "${n.title}"?`);
      if (!ok) return;

      try {
        await api(`/notes/${n.id}`, { method: "DELETE" });
        await loadNotes();
      } catch (e) {
        setMsg(els.listMsg, `Delete failed: ${e.status} ${JSON.stringify(e.data)}`, true);
      }
    });

    els.notesList.appendChild(li);
  }
}

async function loadNotes() {
  setMsg(els.listMsg, "Loading...");
  try {
    const r = await api("/notes");
    renderNotes(r.data || []);
    setMsg(els.listMsg, r.data?.length ? "" : "No notes yet.");
  } catch (e) {
    setMsg(els.listMsg, `Load failed: ${e.status} ${JSON.stringify(e.data)}`, true);
  }
}

els.refreshBtn.addEventListener("click", loadNotes);

els.cancelBtn.addEventListener("click", resetForm);

els.form.addEventListener("submit", async (ev) => {
  ev.preventDefault();
  setMsg(els.formMsg, "");

  const payload = {
    title: els.title.value.trim(),
    content: els.content.value ?? "",
  };

  if (!payload.title) {
    setMsg(els.formMsg, "Title is required.", true);
    return;
  }

  const id = els.noteId.value;

  try {
    if (!id) {
      await api("/notes", { method: "POST", body: JSON.stringify(payload) });
      setMsg(els.formMsg, "Created.");
    } else {
      await api(`/notes/${id}`, { method: "PUT", body: JSON.stringify(payload) });
      setMsg(els.formMsg, "Updated.");
    }

    resetForm();
    await loadNotes();
  } catch (e) {
    setMsg(els.formMsg, `Save failed: ${e.status} ${JSON.stringify(e.data)}`, true);
  }
});

// Initial load
loadNotes();
