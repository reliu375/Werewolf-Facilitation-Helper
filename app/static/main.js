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

  var seerElement = document.getElementById('num_seer');
  var numSeer = parseInt(seerElement.value.toString());
  if (isNaN(numSeer))
    numSeer = 0;

  var witchElement = document.getElementById('num_witch');
  var numWitch = parseInt(witchElement.value.toString());
  if (isNaN(numWitch))
    numWitch = 0;

  var hunterElement = document.getElementById('num_hunter');
  var numHunter = parseInt(hunterElement.value.toString());
  if (isNaN(numHunter))
    numHunter = 0;

  var guardElement = document.getElementById('num_guard');
  var numGuard = parseInt(guardElement.value.toString());
  if (isNaN(numGuard))
    numGuard = 0;

  var input_dict = {'wolf': numWolves,
                    'villager': numVillagers,
                    'seer': numSeer,
                    'witch': numWitch,
                    'hunter': numHunter,
                    'guard': numGuard};

  return input_dict
}

function requestRoles(input) {
  var result;
  $.ajax({
    type: 'GET',
    url: '/distribute_role',
    data: input
  }).done(function(data){
    var roleElement = document.getElementById('role_list');
    roleElement.parentNode.removeChild(roleElement);

    var roleDiv = document.getElementById('role-distribution-list');
    roleDiv.innerHTML="角色分配";
    roleElement = document.createElement('ul');
    roleElement.setAttribute('id', 'role_list');
    for (var ix = 0; ix < data.length; ++ix){
      var s = (ix+1).toString() + ": " + data[ix];
      var li = document.createElement('li');
      li.append(document.createTextNode(s));
      roleElement.appendChild(li);
    }

    roleDiv.appendChild(roleElement);
  });

  return result;
}
