const getUsersApiUrl = 'http://127.0.0.1:5000/api/users'
const getUsersAsyncAwait = async () => {

    let users;
    try {
        users = await fetch(getUsersApiUrl).then((response) => response.json());
        let usershtml = ''
        books.forEach(user => usershtml += `<p>${user.username}</p>`);
        document.getElementById('users-list').innerHTML = bookshtml;
    } catch (e) {
        console.log(e);
    }
    console.log(books);
    // return books;
};
