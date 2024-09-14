document.addEventListener('DOMContentLoaded', function () {

    function setupPagination(sectionId, cardsDataId, cardsPerPage = 6) {
        const cardsDataElement = document.getElementById(cardsDataId);
        const cards = JSON.parse(cardsDataElement.getAttribute('data-cards'));  // Leer los datos JSON
        let currentPage = 1;

        const cardsContainer = document.getElementById(sectionId);
        const pageInfo = document.getElementById(`page-info-${cardsDataId.split('-')[2]}`);

        function displayCards(page) {
            cardsContainer.innerHTML = ""; // Limpiar tarjetas anteriores
            const start = (page - 1) * cardsPerPage;
            const end = start + cardsPerPage;
            const cardsToShow = cards.slice(start, end);

            cardsToShow.forEach(card => {
                const cardElement = document.createElement('div');
                cardElement.classList.add('card');
                cardElement.innerHTML = `<h3>${card.nombre_pais}</h3><h4>${card.nombre}</h4><p><span>${card.item1}</span><span> </span><span>${card.valor1}</span></p><p><span>${card.item2}</span<span> </span><span>${card.valor2}</span></p>`;
                cardsContainer.appendChild(cardElement);
            });

            pageInfo.textContent = `Página ${currentPage} de ${Math.ceil(cards.length / cardsPerPage)}`;
        }

        function nextPage() {
            if (currentPage * cardsPerPage < cards.length) {
                currentPage++;
                displayCards(currentPage);
            }
        }

        function prevPage() {
            if (currentPage > 1) {
                currentPage--;
                displayCards(currentPage);
            }
        }

        // Listeners para los botones de paginación
        document.getElementById(`next-page-${cardsDataId.split('-')[2]}`).addEventListener('click', nextPage);
        document.getElementById(`prev-page-${cardsDataId.split('-')[2]}`).addEventListener('click', prevPage);

        // Mostrar la primera página de tarjetas
        displayCards(currentPage);
    }

    // Configurar paginación para la primera sección
    setupPagination('cards-container-1', 'cards-data-1');

    // Configurar paginación para la segunda sección
    setupPagination('cards-container-2', 'cards-data-2');

});