<?php 
  // Headers
  header('Access-Control-Allow-Origin: *');
  header('Content-Type: application/json');

  include_once '../config/Database.php';
  include_once '../models/ReadData.php';

  // Instantiate DB & connect
  $database = new Database();
  $db = $database->connect();

  // Instantiate object
  $data = new Data($db);

  // Query
  $result = $data->read();
  // Get row count
  $num = $result->rowCount();

  // Check if any queries
  if($num > 0) {
    //Data array
    $data_list = array();

    while($row = $result->fetch(PDO::FETCH_ASSOC)) {
      extract($row);

      $data_item = array(
        'name' => $name,
        'value' => $value
      );

      // Push to "data"
      array_push($data_list, $data_item);
    }

    // Turn to JSON & output
    echo json_encode($data_list);

  } else {
    echo json_encode(
      array('message' => 'No Data Found')
    );
  }