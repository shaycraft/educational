(function(){
    
    var github = function($http){
      
      var getUser = function(username){
            return $http.get("https://api.github.com/users/" + username)
                        .then(function(response){
                           return response.data; 
                        });
      };
      
      var getRepos = function(user){
            return $http.get(user.repos_url)  
                        .then(function(response){
                            return response.data;
                        });
      };

      var getRepoDetails = function(username, reponame) {
        console.log('to be implemented');
          // example url: https://api.github.com/repos/angular/angular
      };
      
      return {
          getUser: getUser,
          getRepos: getRepos,
          getRepoDetails: getRepoDetails
      };
        
    };
    
    var module = angular.module("githubViewer");
    module.factory("github", github);
    
}());