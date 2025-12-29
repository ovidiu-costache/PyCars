document.addEventListener('DOMContentLoaded', function() {
    
    // Logica pentru filtrarea modelelor in functie de marca
    const selectMarca = document.getElementById('selectMarca');
    const selectModel = document.getElementById('selectModel');

    if (selectMarca && selectModel) {
        // Salvam toate optiunile de modele intr-o lista ca sa nu le pierdem
        const toateModelele = Array.from(selectModel.options);

        selectMarca.addEventListener('change', function() {
            const marcaIdSelectata = this.value;

            // Resetam selectia de model la "Toate"
            selectModel.value = "0";

            // Golim lista actuala de modele
            selectModel.innerHTML = '';

            // Adaugam inapoi doar modelele care corespund marcii
            toateModelele.forEach(function(optiune) {
                // Optiunea "Toate modelele" (cu value 0) o pastram mereu
                if (optiune.value === "0") {
                    selectModel.appendChild(optiune);
                } 
                // Daca marca e "Toate" (0), afisam tot
                else if (marcaIdSelectata === "0") {
                    selectModel.appendChild(optiune);
                }
                // Altfel, verificam daca ID-ul marcii din model corespunde cu ce am ales
                else if (optiune.getAttribute('data-make') === marcaIdSelectata) {
                    selectModel.appendChild(optiune);
                }
            });
        });
    }

    console.log("Script incarcat: Filtrare dinamica model activata.");
});

function salveazaLaFavorite() {
    alert("Anunt salvat la favorite!");
}