extern crate regex;
use self::regex::Regex;

struct Point
{
    name : char,
    executed : bool,
}


struct Edge
{
    start : Point,
    end : Point,
}

fn findPointInEdgeList(edgeList : &Vec<Edge>, point_name : char) -> &Point
{
    let mut result = Point {name: 'A', executed: false};

    for edge in edgeList.iter()
    {
        if edge.start.name == point_name
        {
            result = &edge.start;
        }
        else if edge.end.name == point_name
        {
            result = &edge.end;
        }
    }

    result
}

fn createEdgeList(input : String) -> Vec<Edge>
{
    let lines : Vec<_> = input
        .split("\r\n")
        .collect();
    let re = Regex::new(r"Step ([A-Z]) must be finished before step ([A-Z]) can begin.")
        .unwrap();

    let result : Vec<Edge> = Vec::new();
    for line in lines.iter() 
    {
        for cap in re.captures_iter(line)
        {
            println!("{} -> {}", &cap[1], &cap[2]);
        }
    }

    result
}

pub fn problem1()
{
    let file_content = include_str!("./data/input_6_1_tmp.txt").to_string();
    let edges = createEdgeList(file_content);
}