/**
 * Created by Sam on 5/2/2015.
 */

(function() {

    var app = angular.module("githubViewer");

    var RepoController = function($scope, github, $routeParams) {

        var onRepoDetailsComplete = function(data)
        {
            $scope.repodetails = data;
        };

        var onRepoContributorsComplete = function(data) {
            $scope.contributors = data;
        };

        var onError = function (reason) {
            $scope.error = "Could not fetch the data.";
        };

        $scope.reponame = $routeParams.reponame;
        $scope.username = $routeParams.username;

        github.getRepoDetails($scope.username, $scope.reponame).then(onRepoDetailsComplete, onError);
        github.getRepoContributors($scope.username, $scope.reponame).then(onRepoContributorsComplete, onError);
    }

    app.controller("RepoController", ['$scope', 'github', '$routeParams', RepoController]);

})();