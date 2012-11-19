GLClient.controller('AdminCtrl',
    ['$scope', '$http', '$location', 'localization', 'AdminNode',
    'AdminContexts', 'AdminReceivers',
    function($scope, $http, $location, localization, AdminNode, AdminContexts,
      AdminReceivers) {

  // XXX convert this to a directive
  // This is used for setting the current menu in the sidebar
  var current_menu = $location.path().split('/').slice(-1);
  $scope.active = {};
  $scope.active[current_menu] = "active";

  $scope.localization = localization;
  $scope.node_info = localization.node_info;

  $scope.adminNode = new AdminNode();
  $scope.adminNode.$get();

}]);
