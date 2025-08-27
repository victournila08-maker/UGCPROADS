document.addEventListener('DOMContentLoaded', () => {
  const yearSpan = document.getElementById('year');
  if (yearSpan) {
    yearSpan.textContent = new Date().getFullYear();
  }

  const form = document.getElementById('quote-form');
  if (form) {
    form.addEventListener('submit', (e) => {
      if (!form.checkValidity()) {
        // allow browser to display validation errors
        return;
      }
      e.preventDefault();
      alert('Thank you! We\'ll be in touch shortly.');
      form.reset();
    });
  }
});
