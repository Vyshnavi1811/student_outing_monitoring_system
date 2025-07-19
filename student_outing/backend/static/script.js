// Student form handler
document.getElementById('outingForm').addEventListener('submit', async (e) => {
  e.preventDefault();
  const studentId = document.getElementById('studentId').value.trim();
  const action = e.submitter.value;
  const errorEl = document.getElementById('error');

  // Validate student ID: only 5 digits
  const valid = /^[0-9]{5}$/.test(studentId);
  if (!valid) {
    errorEl.textContent = "Invalid Student ID. Only 5 digits allowed.";
    return;
  }

  errorEl.textContent = ''; // Clear error

  const res = await fetch(`/student/${action}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ student_id: studentId })
  });

  const data = await res.json();
  alert(data.message);
});

// Admin Login
document.getElementById('adminForm').addEventListener('submit', function (e) {
  e.preventDefault();
  const password = document.getElementById('adminPass').value;
  if (password === 'admin123') {
    document.getElementById('adminPanel').style.display = 'block';
    alert("Admin access granted");
  } else {
    alert("Incorrect admin password");
  }
});

// View Pending Students
document.getElementById('viewPending').addEventListener('click', async () => {
  const res = await fetch('/admin/pending');
  const pending = await res.json();

  const tableBody = document.querySelector('#pendingTable tbody');
  tableBody.innerHTML = '';

  if (pending.length === 0) {
    alert("No pending students found!");
    return;
  }

  pending.forEach(student => {
    const row = document.createElement('tr');
    row.innerHTML = `
      <td>${student.student_id}</td>
      <td>${new Date(student.out_time).toLocaleString()}</td>
    `;
    tableBody.appendChild(row);
  });
});
// Admin Login (Secure)
document.getElementById('adminForm').addEventListener('submit', async function (e) {
  e.preventDefault();
  const password = document.getElementById('adminPass').value;

  const res = await fetch('/login', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ password })
  });

  const data = await res.json();
  if (res.ok) {
    document.getElementById('adminPanel').style.display = 'block';
    alert(data.message);
  } else {
    alert(data.message);
  }
});

// Logout (optional button if needed)
async function logoutAdmin() {
  await fetch('/logout', { method: 'POST' });
  alert("Logged out");
  document.getElementById('adminPanel').style.display = 'none';
}

// View Student Logs
document.getElementById('viewLogs').addEventListener('click', async () => {
  const studentId = document.getElementById('studentId').value;
  const res = await fetch(`/student/logs/${studentId}`);
  const logs = await res.json();

  const tableBody = document.querySelector('#logTable tbody');
  tableBody.innerHTML = '';

  if (logs.length === 0) {
    alert("No logs found");
    return;
  }

  logs.forEach(log => {
    const row = document.createElement('tr');
    row.innerHTML = `
      <td>${new Date(log.out_time).toLocaleString()}</td>
      <td>${log.in_time ? new Date(log.in_time).toLocaleString() : 'Not yet returned'}</td>
    `;
    tableBody.appendChild(row);
  });
});
