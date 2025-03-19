document.addEventListener('DOMContentLoaded', function () {

    function searchStudents() {
        let input = document.getElementById("searchBar").value.toLowerCase();
        let rows = document.querySelectorAll("#studentsTable tr");

        
        for (let i = 0; i < rows.length; i++) {
            let row = rows[i];
            let cells = row.querySelectorAll("td");
            let text = "";

         
            for (let j = 0; j < cells.length - 1; j++) { 
                text += cells[j].textContent.toLowerCase();
            }

          
            row.style.display = text.includes(input) ? "" : "none";
        }
    }

    document.querySelector("button").addEventListener("click", searchStudents);
});
