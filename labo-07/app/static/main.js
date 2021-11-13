const backendUrl = "http://localhost:5000";
async function onSignIn(googleUser) {
    const profile = googleUser.getBasicProfile();
    const user = {
        id: profile.getId(),
        fullName: profile.getName(),
        email: profile.getEmail(),
    };
    console.log(user);

    const response = await login(user);
    console.log(response);
}

function signOut() {
    var auth2 = gapi.auth2.getAuthInstance();
    auth2.signOut().then(function () {
        console.log("User signed out.");
    });
}

const login = async (profile) => {
    const response = await fetch(backendUrl + "/api/v1/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(profile),
    });
    return response.json();
};

const logout = async () => {
    const response = await fetch(backendUrl + "/api/v1/logout");
    return response.json();
};

const logoutUser = async () => {
    const response = await logout();
    console.log(response);
};
