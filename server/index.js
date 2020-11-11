require("dotenv").config();
const fs = require("fs");
const sqlite3 = require("sqlite3");
const express = require("express");

const dbPath = process.env.DB_PATH;

if (!fs.existsSync(dbPath)) fs.mkdirSync(dbPath);

let db = new sqlite3.Database(dbPath);

const app = express();

app.set("view engine", "pug");
app.set("json spaces", 2);
app.use(express.json());

(async () => {
    await db.get(
        fs.readFileSync("./scripts/sql/createTableArticles.sql", "utf8"),
        (err) => {
            if (err) {
                console.error(err.message);
            } else {
                console.log("[DATABASE] Table Articles OK");
            }
        }
    );

    /*const routes = await filewalker.walk(__dirname + '/routes/');

    routes.forEach((route) => {
        const time = new Date().getMilliseconds();
        require(route.path)(app, db);
        console.log(`[EXPRESS] Loaded route file ${route.name} in ${new Date().getMilliseconds() - time}ms`);
    });*/

    app.get("/", (req, res) => {
        res.render("index");
    });

    app.get("*", (req, res) => {
        res.sendStatus(404);
    });
})();

app.listen(process.env.PORT, "0.0.0.0", () =>
    console.log("[EXPRESS] Server started at port", process.env.PORT)
);
