document.addEventListener("DOMContentLoaded", () => {
    function updateDecorationLineWidth() {
        const decorationLine = document.getElementById('decoration-line');
        const header = document.getElementById('header');

        const headerWidth = header.offsetWidth;
        const bodyWidth = document.body.clientWidth;
        const decorationLineWidth = bodyWidth - headerWidth;

        decorationLine.style.width = `${decorationLineWidth}px`;
    }

    // Initial calculation on page load
    updateDecorationLineWidth();

    // Recalculate on window resize
    window.addEventListener('resize', updateDecorationLineWidth);
});
