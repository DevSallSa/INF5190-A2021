// initialize moduiles
const { src, dest, watch, series } = require("gulp");
const sass = require("gulp-sass")(require('sass'));
const postcss = require("gulp-postcss");
const autoprefixer = require("autoprefixer");
const cssnano = require("cssnano");
const babel = require("gulp-babel");
const terser = require("gulp-terser");
const browsersync = require("browser-sync").create();

// SASS Task
function scssTask() {
    return src("app/scss/style.scss", { sourcemaps: true })
        .pipe(sass())
        .pipe(postcss([autoprefixer, cssnano()]))
        .pipe(dest("dist", { sourcemaps: "." }));
}

// JAVASCRIPT Task
function jsTask() {
    return src("app/static/js/script.js", { sourcemaps: true })
        .pipe(babel({ presets: ["@babel/preset-env"] }))
        .pipe(terser())
        .pipe(dest("dist", { sourcemaps: "." }));
}

// Browser sync
function browserSyncServe(cb) {
    browsersync.init({
        server: {
            baseDir: ".",
        },
        notify: {
            styles: {
                top: "auto",
                bottom: 0,
            },
        },
    });
    cb();
}

function browserSyncReload(cb) {
    browsersync.reload();
    cb();
}

function watchTask() {
    watch("app/templates/**/*.html", browserSyncReload);
    watch(["app/scss/**/*.scss", "app/static/**/*.js"], series(scssTask, jsTask, browserSyncReload));
}

exports.default = series(scssTask, jsTask, browserSyncServe, watchTask);
