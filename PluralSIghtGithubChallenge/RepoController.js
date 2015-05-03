/**
 * Created by Sam on 5/2/2015.
 */

(function() {

    var app = angular.module("githubViewer");

    var RepoController = function($scope, github, $routeParams) {
        $scope.reponame = $routeParams.reponame;
        $scope.username = $routeParams.username;
    }

    app.controller("RepoController", ['$scope', 'github', '$routeParams', RepoController]);

})();