
struct Point {
    x: i32,
    y: i32,
}

struct FieldCoordinate {
    coordinate : Point,
    nearPoints : Vec<Point>
}

fn parseFieldCoordinates(input : String) -> Vec<FieldCoordinate>
{
    let mut field_coordinates : Vec<FieldCoordinate> = Vec::new();
    let parsed_coordinates : Vec<_> = input
        .split(|c: char| c == ' ' || c == '\n' || c == '\r' || c == ',')
        .filter(|v| *v != "")
        .map(|i| i.parse::<i32>().unwrap())
        .collect();

    let mut skip_next : bool = false;
    for i in 0..parsed_coordinates.len()-1
    {
        if skip_next
        {
            skip_next = false;
            continue;
        }

        skip_next = true;

        let point = Point {
            x: parsed_coordinates[i],
            y: parsed_coordinates[i + 1],
        };
        let field_coordinate = FieldCoordinate {
            coordinate : point,
            nearPoints : Vec::new(),
        };

        field_coordinates.push(field_coordinate);


    }
    field_coordinates
}


pub fn problem1()
{
    let file_content = include_str!("./data/input_6_1_tmp.txt").to_string();
    let field_coordinates = parseFieldCoordinates(file_content);

    for c in field_coordinates.iter()
    {
        println!("{}", c.coordinate.x);
    }
}