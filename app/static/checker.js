var roleDict = {
  "wolf": "狼人",
  "villager": "平民",
  "witch": "女巫",
  "seer": "预言家",
  "hunter": "猎人",
  "guard": "守卫",
  "knight": "骑士",
  "idiot": "白痴神",
  "seer!": "通灵师",
  "gravekeeper": "守墓人",
  "copier": "复刻",
  "nightmare wolf": "梦魇",
  "wolf king": "狼王",
  "wolf beauty": "狼美人",
  "mechanical wolf": "机械狼人",
  "hidden wolf": "隐狼",
  "wolf bishop": "种狼"
};

function check(){
  var input_dict = parseInput();
  if (input_dict)
    var result = requestRole(input_dict);
}

function parseInput(){
  var idElement = document.getElementById('game_id');
  var gameId = idElement.value.toString();
  if (isNaN(gameId)){
    error("Please fill in the game ID!");
    return;
  }

  var numElement = document.getElementById('player_num');
  var playerNum = parseInt(numElement.value.toString());
  if (isNaN(playerNum)){
    error("Please fill in the player number!")
    return;
  }

  var input_dict = {'game_id': gameId,
                    'player_num': playerNum,
                   };

  error("");
  return input_dict
}

function error(message) {
  document.getElementById('inputErrorRemind').innerHTML = message;
}

function requestRole(input){
  var result;
  $.ajax({
    type: 'GET',
    url: '/check_role',
    data: input
  }).done(function(data){
    var roleDocument = document.getElementById('role-result');
    roleDocument.innerHTML = '';
    if (data['role'] !== ''){
      roleDocument.innerHTML = "你的身份是：" + roleDict[data['role']];
      var button = document.getElementById("role-checker");
      button.disabled = true;
    } else {
      error('Cannot find your role. Please double check your game ID and/or player number.')
    }
  });
}
