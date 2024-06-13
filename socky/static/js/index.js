document.addEventListener('DOMContentLoaded', () => {
    const selects = document.querySelectorAll('select');
    const nameInput = document.querySelector('#nameInput');
    const consultantSelect = document.querySelector('#consultantSelect');
    const sectionSelect = document.querySelector('#sectionSelect');
    const stateSelect = document.querySelector('#stateSelect');
    const themes = document.querySelectorAll('.theme');
    const resetBtn = document.querySelector('#resetBtn');

    selects.forEach(select => {
        select.addEventListener('change', (event) => {
            if (event.target.value === "") {
                event.target.classList.add('default-selected');
            } else {
                event.target.classList.remove('default-selected');
            }
        });

        if (select.value === "") {
            select.classList.add('default-selected');
        } else {
            select.classList.remove('default-selected');
        }
    });


    function filterThemes() {
        const nameFilter = nameInput.value.toLowerCase().trim();
        const consultantFilter = consultantSelect.value;
        const sectionFilter = sectionSelect.value;
        const stateFilter = stateSelect.value;

        console.log(nameFilter)
        console.log(consultantFilter)
        console.log(sectionFilter)
        console.log(stateFilter)

        themes.forEach((item) => {
            const name = item.querySelector('.theme-name').textContent.toLowerCase();
            const consultant = item.querySelector('.theme-consultant').dataset.id;
            const section = item.querySelector('.theme-section').dataset.id;
            const state = item.querySelector('.theme-state').dataset.id;



            const nameMatch = nameFilter.length === 0 ? true : name.includes(nameFilter);
            const consultantMatch = consultantFilter === "all" || consultantFilter === consultant;
            const sectionMatch = sectionFilter === "all" || sectionFilter === section;
            const stateMatch = stateFilter === "all" || stateFilter === state;

            console.log(nameMatch)
            console.log(consultantMatch)
            console.log(sectionMatch)
            console.log(stateMatch)


            if (nameMatch && consultantMatch && sectionMatch && stateMatch) {
                item.style.display = "block";
            }
            else {
                item.style.display = "none";
            }
        });
    }

    nameInput.addEventListener('input', filterThemes);
    consultantSelect.addEventListener('change', filterThemes);
    sectionSelect.addEventListener('change', filterThemes);
    stateSelect.addEventListener('change', filterThemes);
});