// Actors stuff
if (document.title === "Leikarar") {
	for (let i = 0; i < 4; i++) {
		let elActor = document.getElementById("actor-" + i);
		let elActorImg = elActor.childNodes[1];
		let elActorText = elActor.childNodes[3];
		let actorImage = true;
		let elActorHeight = elActor.clientHeight;

		elActor.addEventListener("click", function() {
			if (actorImage) {
				elActorImg.style.display = "none";
				elActorText.style.display = "block";
				actorImage = false;
				elActor.style.height = elActorHeight;
			} else {
				elActorImg.style.display = "block";
				elActorText.style.display = "none";
				actorImage = true;
				elActor.style.height = "inital";
			}
		}, false);
	};
};

// Validate dótarí
if (document.title === "Hafa Samband") {
	var validator = new FormValidator("contactForm", [{
			name: "mail",
			rules: "required|valid_email",
			display: "netfang"
		}, {
			name: "name",
			rules: "alpha",
			display: "nafn"
		}, {
			name: "comment",
			rules: "required",
			display: "fyrirspurn"
		}], function(errors) {
			console.log(errors);
			if (errors.length > 0) {
				errors.forEach(function(error) {
					error.element.value = "";
					error.element.placeholder = error.message;
				});
			}
	});

	validator.setMessage("required", "Þú verður að fylla inní þennan reit");
	validator.setMessage("valid_email", "Þú verður að slá inn gilt netfang");
	validator.setMessage("alpha", "Þú mátt ekki nota tölustafi hér");
};