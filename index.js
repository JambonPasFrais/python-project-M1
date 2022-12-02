const express = require("express");
const app = express();
const http = require("http").Server(app);
const path = require("path");

let PORT = process.env.PORT || 4444;
//Start serveur
http.listen(PORT, () => {
    console.log("Serveur lancé sur http://localhost:" + PORT);
});

app.get("/", (req, res) => {
    res.sendFile(__dirname + "/index.html");
});

app.use("/assets", express.static(__dirname + "/assets"));
app.use("/", express.static(__dirname));

app.get("/:folder/:name", (req, res) => {
    // if name is not a html file, redirect to index

    if (req.params.name.indexOf(".html") === -1 && req.params.name.split(".").length > 1) {
        res.redirect("/");
    } else {
        res.sendFile(path.join(__dirname, req.params.folder + "/" + req.params.name));
    }
});
