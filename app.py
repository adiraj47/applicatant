import gspread
from flask import jsonify, Flask
from oauth2client.service_account import ServiceAccountCredentials
from flask_cors import CORS, cross_origin
from flask_restful import Resource, reqparse, Api

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("gsheetKey.json", scope)
client = gspread.authorize(creds)
sheet = client.open("job-portal").worksheet("Sheet7")
app = Flask(__name__)
CORS(app)
api = Api(app)
class Apllicant(Resource):
    def post(self):
        """
        The function is used to append the data in the google sheet for the applicant side.
        """
        user_data_parse = reqparse.RequestParser()
        user_data_parse.add_argument("username", required=True, type=str)
        user_data_parse.add_argument("password", required=True, type=str)
        user_data_parse.add_argument("name", required=True, type=str)
        user_data_parse.add_argument("email", required=True, type=str)
        user_data_parse.add_argument("phone", required=True, type=int)
        user_data_parse.add_argument("Gender", required=True, type=str)
        user_data_parse.add_argument("city", required=True, type=str)
        user_data_parse.add_argument("address", required=True, type=str)
        user_data_parse.add_argument("Primary_skill", required=True, type=str)
        user_data_parse.add_argument("Additional_skills", type=str)
        user_data_parse.add_argument("Experience", required=True, type=int)
        user_data_parse.add_argument("Current_Salary", required=True, type=int)
        user_data_parse.add_argument("Expected_salary", type=int)
        user_data_parse.add_argument("job_loc_1", required=True, type=str)
        user_data_parse.add_argument("job_loc_2", required=True, type=str)
        user_data_parse.add_argument("job_loc_3", required=True, type=str)
        user_data_parse.add_argument("job_post_pre_1", required=True, type=str)
        user_data_parse.add_argument("job_post_pre_2", required=True, type=str)
        user_data_parse.add_argument("job_post_pre_3", required=True, type=str)
        user_data_parse.add_argument("Linkdin_link", type=str)

        args = user_data_parse.parse_args()
        username = args["username"]
        password = args["password"]
        name = args["name"]
        email_id = args["email"]
        phone = str(args["phone"])
        city = args["city"]
        address = args["address"]
        primary_skill = args["Primary_skill"]
        additional_skills = args["Additional_skills"]
        experience = str(args["Experience"])
        current_salary = str(args["Current_Salary"])
        expected_salary = str(args["Expected_salary"])
        job_loc_1 = args["job_loc_1"]
        job_loc_2 = args["job_loc_2"]
        job_loc_3 = args["job_loc_3"]
        job_post_pref_1 = args["job_post_pre_1"]
        job_post_pref_2 = args["job_post_pre_2"]
        job_post_pref_3 = args["job_post_pre_3"]
        linkdin_link = args["Linkdin_link"]

        print(args.values())

        sheet.append_row([username, password, name, email_id, phone, city, address, primary_skill, additional_skills,
                          experience, current_salary, expected_salary, job_loc_1, job_loc_2, job_loc_3, job_post_pref_1,
                          job_post_pref_2, job_post_pref_3, linkdin_link])  # To enter the details in the sheet
        return {"responses": "Data recorded"}


api.add_resource(Apllicant, "/applicant")
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)