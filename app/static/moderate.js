function distribute(){
  var input_dict = parseInput();
  var result = requestRoles(input_dict);
}

function parseInput(){
  var wolfElement = document.getElementById('num_wolves');
  var numWolves = parseInt(wolfElement.value.toString());
  if (isNaN(numWolves))
    numWolves = 0;

  var villagerElement = document.getElementById('num_villagers');
  var numVillagers = parseInt(villagerElement.value.toString());
  if (isNaN(numVillagers))
    numVillagers = 0;

  // Special villagers
  var seerElement = document.getElementById('seer');
  var numSeer = (seerElement.checked) ? 1 : 0;

  var witchElement = document.getElementById('witch');
  var numWitch = (witchElement.checked) ? 1 : 0;

  var hunterElement = document.getElementById('hunter');
  var numHunter = (hunterElement.checked) ? 1 : 0;

  var guardElement = document.getElementById('guard');
  var numGuard = (guardElement.checked) ? 1 : 0;

  var knightElement = document.getElementById('knight');
  var numKnight = (knightElement.checked) ? 1 : 0;

  var idiotElement = document.getElementById('idiot');
  var numIdiot = (idiotElement.checked) ? 1 : 0;

  var graveElement = document.getElementById('gravekeeper');
  var numGrave = (graveElement.checked) ? 1 : 0;

  var copyElement = document.getElementById('copier');
  var numCopy = (copyElement.checked) ? 1 : 0;

// Special Wolves
  var specialWolvesElement = document.getElementById('special_wolves');
  var regExp = /[(/]/;
  var specialWolfList = specialWolvesElement.value.toLowerCase().split(regExp);
  specialWolfList.pop();

  var input_dict = {'wolf': numWolves,
                    'villager': numVillagers,
                    'seer': numSeer,
                    'witch': numWitch,
                    'hunter': numHunter,
                    'guard': numGuard,
                    'knight': numKnight,
                    'idiot': numIdiot,
                    'gravekeeper': numGrave,
                    'copier': numCopy,
                    'special_wolf': specialWolfList };
  return input_dict
}

function requestRoles(input) {
  input['game_type'] = 'werewolf';
  var result;
  $.ajax({
    type: 'POST',
    url: '/distribute_role',
    data: input
  }).done(function(data){
    console.log(data);
    var roleElement = document.getElementById('role_list');
    roleElement.parentNode.removeChild(roleElement);

    var roleDiv = document.getElementById('role-distribution-list');
    roleDiv.innerHTML="角色分配<br>Game ID: " + data['game_id'];
    roleElement = document.createElement('ul');
    roleElement.setAttribute('id', 'role_list');
    for (var ix = 0; ix < data['roles'].length; ++ix){
      var s = (ix+1).toString() + ": " + data['roles'][ix];
      var li = document.createElement('li');
      li.append(document.createTextNode(s));
      roleElement.appendChild(li);
    }

    roleDiv.appendChild(roleElement);
  });

  return result;
}
