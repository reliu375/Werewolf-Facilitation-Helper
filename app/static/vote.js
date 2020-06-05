function vote() {
  var input_dict = parseCastVoteInput();
  if (input_dict){
    var result = castVote(input_dict);
  }
}

function checkVote() {
  var input_dict = parseCheckVoteInput();
  if (input_dict){
    var result = getVote(input_dict);
  }
}

function parseCastVoteInput() {
  var idElement = document.getElementById('game_id');
  var gameId = idElement.value.toString();
  if (isNaN(gameId)){
    error("Please fill in the game ID!", 'inputErrorRemind');
    return;
  }

  var numElement = document.getElementById('player_num');
  var playerNum = parseInt(numElement.value.toString());
  if (isNaN(playerNum)){
    error("Please fill in the player number!", 'inputErrorRemind')
    return;
  }

  var dayElement = document.getElementById('day');
  var day = parseInt(dayElement.value.toString());
  if (isNaN(playerNum)){
    error("Please fill in the day!", 'inputErrorRemind')
    return;
  }

  var pk = (document.getElementById('pk').value.checked) ? 1 : 0;

  var voteForElement = document.getElementById('vote_for');
  var voteFor = parseInt(voteForElement.value.toString());
  if (isNaN(voteFor)){
    voteFor = 0;
  }

  var input_dict = {'game_id': gameId,
                    'player_num': playerNum,
                    'day': day,
                    'pk': pk,
                    'vote_for': voteFor
                   };

  error("", 'inputErrorRemind');
  return input_dict

}

function parseCheckVoteInput() {

  var idElement = document.getElementById('game_id2');
  var gameId = idElement.value.toString();
  if (isNaN(gameId)){
    error("Please fill in the game ID!", 'inputErrorRemind2');
    return;
  }

  var dayElement = document.getElementById('day2');
  var day = parseInt(dayElement.value.toString());
  if (isNaN(day)){
    error("Please fill in the day!", 'inputErrorRemind2')
    return;
  }

  var pk = (document.getElementById('pk2').value.checked) ? 1 : 0;

  var input_dict = {'game_id': gameId,
                    'day': day,
                    'pk': pk,
                   };

  error("", 'inputErrorRemind2');
  return input_dict
}

function castVote(input){
  var result;
  $.ajax({
    type: 'POST',
    url: '/cast_vote',
    data: input
  }).done(function(data){
    console.log(data);
    if (parseInt(data['success']) == 1){
      error('Your vote is recorded.', 'inputErrorRemind')
    } else {
      error('There is something wrong with your vote! Try again.', 'inputErrorRemind')
    }
  });
}

function error(message, id) {
  document.getElementById(id).innerHTML = message;
}

function getVote(input){
  var result;
  $.ajax({
    type: 'GET',
    url: '/get_vote',
    data: input
  }).done(function(data){
    console.log(data);
    if (parseInt(data['success']) == 1){
      console.log("hi");
      var resultElement = document.getElementById('vote-list');
      resultElement.parentNode.removeChild(resultElement);
      var resultParent = document.getElementById('vote-output');
      resultElement = document.createElement('ul');
      resultElement.setAttribute('id', 'vote-list');

      for (key in data['votes']){
        var k;
        if (key == 0)
          k = "弃票";
        else
          k = key;
        var str = k.toString() + ": " + data['votes'][key];
        var li = document.createElement('li');
        li.append(document.createTextNode(str));
        resultElement.appendChild(li);
      }

      resultParent.appendChild(resultElement);
    } else {
      error('There is something wrong with your query! Try again.', 'inputErrorRemind2')
    }
  });
}
