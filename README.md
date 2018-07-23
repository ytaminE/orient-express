# Orient-Express
ECE1779-A3-Function as a Service(AWS Lambda function)

API Gateway Link: https://fk03bgn9ul.execute-api.us-east-1.amazonaws.com/dev

## How to test locally
```
source venv/bin/activate
./start.sh
```
## How to deploy
Please include the instance folder and set up the AWS environment in the format below
```python
DEBUG = True # Turns on debugging features in Flask
BCRYPT_LEVEL = 12 # Configuration for the Flask-Bcrypt extension
MAIL_FROM_EMAIL = "test@test.com" # For use in application emails
UPLOAD_FOLDER = '/'
S3_FOLDER = '/'

SECRET_KEY = ''
STRIPE_API_KEY = ''

AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''

IMAGE_BUCKET_NAME = 'your s3 bucket name'
```

```
zappa deploy
```
## How to update 
```
zappa update
```
## How to update static files in S3?
```
python upload_s3.py
```
After uploading successfully, please change the metadata of the "css" folder in s3 and write content-type as "text/css".


## Solution for TwoSum

Python
```python
def TwoSum(nums):
    target = nums[-1]
    nums = nums[0:-1]
    map = {}
    for i in range(len(nums)):
        if nums[i] not in map:
            map[target - nums[i]] = i
        else:
            return map[nums[i]], i
    return "No result found"
```

Ruby
```ruby
class Solution
    def TwoSum(nums)
      target = nums[nums.size-1]
      numbers_hash = {}
      nums.each_with_index do |number, index|
        numbers_hash[index] = number
        hash_key = ((numbers_hash.select { |k,v| v == (target - number) }.keys) - [index])
        hash_key.empty? ? false : (return [hash_key, index].flatten)
      end
      return "Couldn't find target value"
    end
end
```

JavaScript
```javascript
module.exports={
    TwoSum:function(){
        var nums = arguments[0];
        var target = nums[nums.length-1];
        nums = nums.slice(0,nums.length-1)
        var saved={}
        var result=[]
        for(i=0; i< nums.length; i++){
            if(saved.hasOwnProperty(nums[i])){
                result[0] = saved[nums[i]];
                result[1] = i;
                return result
              }
        saved[target - nums[i]] = i
        }
        return "No result found";
    }
}
```

Java
```java
public class Solution {
	  public int[] twoSum(int[] numbers, int target) {
		int[] result = new int[2];
		Map<Integer, Integer> map = new HashMap<Integer, Integer>();
		for (int i = 0; i < numbers.length; i++) {
			if (map.containsKey(target - numbers[i])) {
				result[1] = i + 1;
				result[0] = map.get(target - numbers[i]);
				return result;
			}
			map.put(numbers[i], i + 1);
		}
		return result;
	}

    public static void main(String[] args) {
	  	int[] res = new int[2];
	  	int[] numbers = {2,7,11,15,9};
	  	int target = 9;
	  	res = twoSum(numbers, target);
	  	for(int i:res) {
			System.out.println(i);
		}
    }
}
```


# Screenshot
![](https://raw.githubusercontent.com/fssq1993/markdown_photos/master/oriental-express/editor.jpg)
![](https://raw.githubusercontent.com/fssq1993/markdown_photos/master/oriental-express/problemsList.jpg)
