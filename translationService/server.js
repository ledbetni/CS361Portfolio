const axios = require("axios");
const express = require("express");
var bodyParser = require('body-parser')

// initialize express server
const app = express();
app.use(express.json({limit: '50mb', extended: true, parameterLimit: 50000}));
app.use(express.urlencoded({limit: '50mb', extended: true, parameterLimit: 50000}));

const PORT = 4500;		// default port is set to 4500 but you can change this
app.listen(PORT, () => console.log(`Server running on port ${PORT}`)
);

// given some text responds witht he text translated
// simply send a POST request with text to translate in the body.
app.post("/translate", async (req, res) => {
	try {
		const translateText = req.body.text;
		console.log(translateText)
		

		// send request to libre translate api
		const translateResponse = await axios.post(
			"https://libretranslate.de/translate", {
				q: translateText,
				source: "en",
				target: "es",
				format: "text"
			}
		);
		console.log(translateResponse.status)
		console.log(translateResponse.data)
		if (translateResponse.status === 200) {
			res.status(200).json({translated: translateResponse.data.translatedText})
		} else {
			res.sstatus(400).json({message: "there was a problem when tryign to request information from the translator API."})
		}
	} catch (error) {
		console.error(error);
		return res.status(400).json({ message: "error" })
	}
});