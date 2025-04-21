const input = document.getElementById("cityInput");
const suggestionsBox = document.getElementById("suggestions");
let debounceTimeout = null;

function fetchSuggestions(query) {
    /**
     * @brief Fetches location suggestions from the Nominatim API.
     *
     * @param {string} query - The string entered by the user.
     *
     * This function sends a GET request to the Nominatim API to retrieve up to 5 location suggestions.
     * It then populates the suggestion box with clickable options.
     */

    fetch(`https://nominatim.openstreetmap.org/search?q=${encodeURIComponent(query)}&format=json&addressdetails=1&limit=5`)
        .then(res => res.json())
        .then(data => {
            suggestionsBox.innerHTML = "";
            if (data.length === 0) {
                suggestionsBox.style.display = "none";
                return;
            }

            data.forEach(place => {
                const displayName = place.display_name;
                const item = document.createElement("div");
                item.textContent = displayName;
                item.classList.add("suggestion-item")
                item.addEventListener("click", () => {
                    input.value = displayName;
                    suggestionsBox.style.display = "none";
                });
                suggestionsBox.appendChild(item);
            });

            suggestionsBox.style.display = "block";
        })
        .catch(err => {
            console.error("Error obteniendo sugerencias:", err);
            suggestionsBox.style.display = "none";
        });
}

input.addEventListener("input", () => {
    /**
     * @brief Handles the input event with a debounce delay.
     *
     * The listener waits until the user stops typing for 500 milliseconds before triggering the API call.
     */

    const query = input.value.trim();
    if (debounceTimeout) clearTimeout(debounceTimeout);

    if (query.length < 3) {
        suggestionsBox.style.display = "none";
        return;
    }

    debounceTimeout = setTimeout(() => {
        fetchSuggestions(query);
    }, 500);
});

document.addEventListener("click", (e) => {
    /**
     * @brief Closes the suggestion box if the user clicks outside of it.
     */
    if (!suggestionsBox.contains(e.target) && e.target !== input) {
        suggestionsBox.style.display = "none";
    }
});
