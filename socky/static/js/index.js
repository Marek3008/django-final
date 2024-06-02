document.addEventListener('DOMContentLoaded', () => {
    const selects = document.querySelectorAll('select');

    selects.forEach(select => {
        select.addEventListener('change', (event) => {
            if (event.target.value === "") {
                event.target.classList.add('default-selected');
            } else {
                event.target.classList.remove('default-selected');
            }
        });

        // Initial check to apply the correct color
        if (select.value === "") {
            select.classList.add('default-selected');
        } else {
            select.classList.remove('default-selected');
        }
    });
});