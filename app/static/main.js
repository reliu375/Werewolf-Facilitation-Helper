function distribute(){
  var input_dict = parseInput();
}

function parseInput(){
  var wolfElement = document.getElementById('num_wolves');
  var numWolves = parseInt(wolfElement.value.toString());

  var villagerElement = document.getElementById('num_villagers');
  var numVillagers = parseInt(villagerElement.value.toString());

  var seerElement = document.getElementById('num_seer');
  var numSeer = parseInt(seerElement.value.toString());

  var witchElement = document.getElementById('num_witch');
  var numWitch = parseInt(witchElement.value.toString());

  var hunterElement = document.getElementById('num_hunter');
  var numHunter = parseInt(hunterElement.value.toString());

  var guardElement = document.getElementById('num_guard');
  var numGuard = parseInt(guardElement.value.toString());

  var input_dict = {'wolves': numWolves,
                    'villagers': numVillagers,
                    'seer': numSeer,
                    'witch': numWitch,
                    'hunter': numHunter,
                    'guard': numGuard};

  console.log(input_dict)
  return input_dict
}
