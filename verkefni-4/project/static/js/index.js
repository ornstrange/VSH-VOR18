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
}