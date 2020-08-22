function assign(){
  var textArea = document.getElementById('assign');
  var listOfNames = textArea.value.split("\n");
  distribute(listOfNames)
}

function distribute(names){
    var roleElement = document.getElementById('seat_list');
    roleElement.parentNode.removeChild(roleElement);

    var roleDiv = document.getElementById('seat-distribution-list');
    roleDiv.innerHTML="座位分配:<br>";
    roleElement = document.createElement('ul');
    roleElement.setAttribute('id', 'seat_list');

    // shuffle the list
    shuffle(names)
    
    for (var ix = 0; ix < names.length; ++ix){
      var s = (ix+1).toString() + ": " + names[ix];
      var li = document.createElement('li');
      li.append(document.createTextNode(s));
      roleElement.appendChild(li);
    }

    roleDiv.appendChild(roleElement);
}
    
function shuffle(arr) {
  // https://medium.com/@nitinpatel_20236/how-to-shuffle-correctly-shuffle-an-array-in-javascript-15ea3f84bfb
  for(let i = arr.length - 1; i > 0; i--){
    const j = Math.floor(Math.random() * i);
    const temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
  }
}