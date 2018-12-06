
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

fn getMaxCoordinates( coordinates : &Vec<FieldCoordinate>) -> Vec<i32>
{
    let mut max_value_x : i32 = 0;
    let mut max_value_y : i32 = 0;
    for c in coordinates.iter()
    {
        if c.coordinate.x > max_value_x{
            max_value_x = c.coordinate.x;
        }
        if c.coordinate.y > max_value_y {
            max_value_y = c.coordinate.y;
        }
    }

    let mut result : Vec<i32> = Vec::new();
    result.push(max_value_x);
    result.push(max_value_y);

    result
}

fn createGrid(max_x : i32, max_y : i32) -> Vec<Point>
{
    let mut result : Vec<Point> = Vec::new();
    for y in 0..max_y {

        for x in 0..max_x {
            let mut new_point = Point {
                x: x,
                y: y,
            };

            result.push(new_point);
        }
    }

    result
}

fn calcDistanceBetweenPoints(point1 : &Point, point2 : &Point) -> i32
{
    let dist_x = point1.x - point2.x;
    let dist_y = point1.y - point2.y;
    let distance = dist_x.abs() + dist_y.abs();
    distance
}

fn calcDistances(grid : &Vec<Point>, field_coordinates : &mut Vec<FieldCoordinate>)
{
    for p in grid.iter()
    {
        let mut smallest_distance : i32 = 50000;
        let mut point_with_smallest_dist_index : usize = 0;
        let mut shared_point : bool = false;

        let mut index : usize = 0;
        for fc in field_coordinates.iter()
        {
            let distance = calcDistanceBetweenPoints(&p, &fc.coordinate);
            if distance < smallest_distance
            {
                smallest_distance = distance;
                point_with_smallest_dist_index = index;
            }
            else if distance == smallest_distance
            {
                shared_point = true;
                break;
            }
            index += 1;
        }

        if !shared_point
        {
            let point = Point {
                x: p.x,
                y: p.y,
            };
            field_coordinates[point_with_smallest_dist_index].nearPoints.push(point);
        }
    }

}

fn getBiggestField(field_coordinates : &Vec<FieldCoordinate>) -> usize
{
    let mut field_size : usize = 0;
    for f in field_coordinates.iter() {
        if f.nearPoints.len() > field_size {
            field_size = f.nearPoints.len()
        }
    }

    field_size
}


pub fn problem1()
{
    let file_content = include_str!("./data/input_6_1_tmp.txt").to_string();
    let mut field_coordinates = parseFieldCoordinates(file_content);
    let max_coords = getMaxCoordinates(&field_coordinates);
    let grid = createGrid(max_coords[0], max_coords[1]);
    calcDistances(&grid, &mut field_coordinates);

    println!("biggest field {}", getBiggestField(&field_coordinates));
}