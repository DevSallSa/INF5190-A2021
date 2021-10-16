console.log("Mounted !");

// Appel AJAX avec fetch()
const getBookById = async (id) => {
    let book;
    /**
     * TODO: Utiliser fetch() pour une appelle AJAX au backend
     * et retourner les informations d'un livre en particulier
     * ref: https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API
     * youtube: https://www.youtube.com/watch?v=RvYYCGs45L4&ab_channel=Fireship
     * youtube 2 : https://www.youtube.com/watch?v=ITogH7lJTyE&ab_channel=Fireship
     */
    const button = document.getElementById(`button-${id}`);
    const container = document.getElementById(`container-${id}`);
    const content = document.getElementById(`content-${id}`);

    if (!button.classList.contains("activated")) {
        try {
            book = await fetch(`http://localhost:5000/api/v1/book/${id}`).then((response) => response.json());
        } catch (e) {
            console.log(e);
        }
        button.classList.add("activated");
        content.innerHTML = "Sommaire: " + book.sommaire;
        button.innerHTML = "See less"
    } else {
        button.innerHTML = "See more"
    }
    container.classList.toggle("hidden");

    return book;
};

const getBooksClassic = () => {
    let books;
    fetch("http://localhost:5000/api/v1/books")
        .then((response) => response.json())
        .then((data) => {
            console.log(books);
            books = data.message;
        })
        .catch((err) => console.log(err));
    return books;
};

const getBookByIdClassic = (id) => {
    let book;
    fetch(`http://localhost:5000/api/v1/book/${id}`)
        .then((response) => response.json())
        .then((data) => {
            console.log(books);
            book = data.message;
        })
        .catch((err) => console.log(err));

    return book;
};

const getBooksAsyncAwait = async () => {
    let books;
    try {
        books = await fetch("http://localhost:5000/api/v1/books").then((response) => response.json());
    } catch (e) {
        console.log(e);
    }
    return books;
};
