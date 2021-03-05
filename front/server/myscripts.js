fetch("http://127.0.0.1:5000/Montpellier/stations/JACOU")
.then(response => response.json())
.then(response => document.getElementById("lol").innerHTML = response[0].Ville+" "+response[0].Station)
.catch(error => alert("Erreur : " + error));