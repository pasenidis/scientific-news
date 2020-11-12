module.exports = {
    entry: "./static/main.js",
    output: {
        path: __dirname + "/views/js",
        filename: "bundle.js",
    },
    module: {
        rules: [
            {
                test: /\.css$/,
                use: ["style-loader", "css-loader"],
            },
            {
                test: /\.(png|jpg)$/,
                loader: "url-loader",
            },
        ],
    },
};
