(function () {

    var app = angular.module("githubViewer");

    var UserController = function ($scope, github, $location, $routeParams) {

        var onUserComplete = function (data) {
            $scope.user = data;
            github.getRepos($scope.user).then(onRepos, onError);
        };

        var onRepos = function (data) {
            $scope.repos = data;
        };

        var onError = function (reason) {
            $scope.error = "Could not fetch the data.";
        };


        $scope.username = $routeParams.username;
        $scope.repoSortOrder = "-stargazers_count";
        github.getUser($scope.username).then(onUserComplete, onError);

        $scope.getRepoUrl = function(username, reponame) {
            $location.path("/repo/" + username + "/" + reponame);
        }
    };

    app.controller("UserController", UserController);

})();