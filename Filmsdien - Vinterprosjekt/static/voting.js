document.querySelectorAll("#favorittSection form").forEach((form) => {
    form.addEventListener("submit", async (event) => {
        event.preventDefault();
        const button = form.querySelector("button");
        const status = document.querySelector("#stemmeStatus");
        button.disabled = true;
        status.textContent = "";

        try {
            const body = new URLSearchParams();
            document.querySelectorAll("#favorittSection form").forEach((currentForm) => {
                body.append("current_films", currentForm.dataset.film);
            });
            const response = await fetch(form.action, {
                method: form.method,
                headers: { Accept: "application/json" },
                body,
            });
            const result = await response.json();

            if (!response.ok) {
                throw new Error(result.error || "Stemmen kunne ikke registreres.");
            }

            document.querySelectorAll("#favorittSection .filmvalg").forEach((card, index) => {
                const film = result.filmer[index];
                const score = card.querySelector(".film-poeng");
                const voteForm = card.querySelector("form");
                card.querySelector("h1").textContent = film.navn;
                card.querySelector(".indexPoster").src = film.bilde;
                card.querySelector(".indexPoster").alt = `Poster for ${film.navn}`;
                score.dataset.film = film.navn;
                score.textContent = film.poeng;
                voteForm.action = film.vote_url;
                voteForm.dataset.film = film.navn;
            });

            const leaderboard = document.querySelector("#topplisteListe");
            leaderboard.replaceChildren(
                ...result.favoritter.map((film) => {
                    const entry = document.createElement("div");
                    entry.dataset.film = film.navn;

                    const name = document.createElement("h2");
                    name.textContent = film.navn;
                    entry.append(name);

                    const score = document.createElement("p");
                    score.textContent = `Poeng: ${film.poeng}`;
                    entry.append(score);

                    return entry;
                }),
            );
        } catch (error) {
            status.textContent = error.message;
        } finally {
            button.disabled = false;
        }
    });
});
