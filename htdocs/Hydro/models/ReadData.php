<?php 
  class Data {
    // DB stuff
    private $conn;
    private $table = 'data_tumbuhan';

    // Post Properties
    public $name;
    public $value;

    // Constructor with DB
    public function __construct($db) {
      $this->conn = $db;
    }

    // Get Posts
    public function read() {
      // Create query
      $query = 'SELECT p.name, p.value FROM ' . $this->table . ' p ';
      
      // Prepare statement
      $stmt = $this->conn->prepare($query);

      // Execute query
      $stmt->execute();

      return $stmt;
    }
  }