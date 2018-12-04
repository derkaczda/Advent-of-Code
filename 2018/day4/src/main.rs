extern crate chrono;
use chrono::{NaiveDate, NaiveDateTime};
use std::collections::HashMap;

fn readFileIntoHashMap(filePath: &str) -> HashMap<&str, i8>
{
    let mut dictionary = HashMap::new();

    dictionary.insert(
        "test",
        1
    );

    dictionary
}

fn main() 
{

    let inputFilePath = "./puzzleinput.txt";
    readFileIntoHashMap(&inputFilePath);

}