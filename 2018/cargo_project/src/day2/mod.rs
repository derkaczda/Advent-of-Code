use std::collections::HashMap;

fn get_nth_char(string: &str, n: usize) -> char
{
    let result = string.chars().nth(n).unwrap();
    result
}

pub fn problem1()
{
    let file_content = include_str!("data/input2_1.txt");
    let split_content = file_content
        .split("\n")
        .collect::<Vec<&str>>();

    for line in split_content.iter() 
    {
        let mut current_char : char = 'a';
        let mut char_count : i8 = 0;

        let mut hash_map = HashMap::new();

        for i in 0..line.len() 
        {
            let tmp_char = get_nth_char(line, i);

            if(hash_map.contains_key(&tmp_char))
            {
                /*let tmp_count = hash_map.get(&tmp_char).unwrap();
                let mut new_count = tmp_count + 1;
                println!("tmp_count {}", new_count);
                hash_map.insert(tmp_char, new_count);*/

                if let Some(x) = hash_map.get_mut(&tmp_char) {
                    *x += 1
                }
            }
            else 
            {
                hash_map.insert(
                    tmp_char,
                    1
                );
            }
        }

        println!("----------------------------\n");
        for(k, v) in hash_map.iter() {
            println!("Key {} Value {} \n", k,v);
        }
    }

}