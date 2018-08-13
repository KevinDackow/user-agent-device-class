<?php
$GSM_LIB_PATH = '/home/kevin/documents/git_projects/research/software/lib';
require("$GSM_LIB_PATH/gsm.php");

//instantiate a gsm and the device to query
$gsm = new gsm();
$srch_dev = "";

if (count($argv) < 3)
{
    echo "Usage: php get_dev_json.php <output_file_path> <device name>";
    exit(1);
}

$output_file = $argv[1];
$arr = array_slice($argv, 2);

#creates device string from space separated terminal input
foreach($arr as $value)
{
    $tmp = $srch_dev.$value;
    $srch_dev = $tmp." ";
}
$srch_dev = substr($srch_dev, 0, -1);
#searches for the device and returns the top results
$data = $gsm->search($srch_dev);
$dev_ids = array();

//map the device name to the device specific id
foreach($data["data"] as $device)
{
    $dev_ids[$device["title"]] = $device["slug"];
}

//get most similar device to searched dev
$similarity = 0;
$max_sim = 0;
$max_dev_name= "";
$max_dev_id = "";

foreach($dev_ids as $dev_name => $dev_id)
{
    similar_text($srch_dev, $dev_name, $similarity);
    if ($similarity > $max_sim)
    {
        $max_sim = $similarity;
        $max_dev_name = $dev_name;
        $max_dev_id = $dev_id;    
    }
}
$dat = $gsm->detail("$max_dev_id");
// Convert to JSON and export to given output file
header('Content-Type: application/json');
file_put_contents("$output_file.json", json_encode($dat, JSON_PRETTY_PRINT));
?>
