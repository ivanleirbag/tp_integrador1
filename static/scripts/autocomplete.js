// static/scripts/autocomplete.js

const input = document.getElementById("cityInput");
const suggestionsBox = document.getElementById("suggestions");
let debounceTimeout = null;

function fetchSuggestions(query) {
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
    if (!suggestionsBox.contains(e.target) && e.target !== input) {
        suggestionsBox.style.display = "none";
    }
});
