# Example
# Import job applications from a CSV File (created via Google Forms) to "Job Application"

import csv

import asyncio

from frappeclient import FrappeClient

NAME = 2
EMAIL = 3
INTRODUCTION = 4
THOUGHTS_ON_COMPANY = 5
LIKES = 6
LINKS = 7
PHONE = 8


async def sync():
    print("logging in...")
    client = FrappeClient("https://xxx.frappecloud.com", "xxx", "xxx")
    with open("jobs.csv", "r") as jobsfile:
        reader = csv.reader(jobsfile, delimiter='\t')
        for row in reader:
            print(row)
            if row[0] == "Timestamp":
                continue

            print("finding " + row[EMAIL])
            name = await client.get_value("Job Applicant", "name", {"email_id": row[EMAIL]})

            if name:
                doc = await client.get_doc("Job Applicant", name["name"])
            else:
                doc = {"doctype": "Job Applicant"}

            doc["applicant_name"] = row[NAME]
            doc["email_id"] = row[EMAIL]
            doc["introduction"] = row[INTRODUCTION]
            doc["thoughts_on_company"] = row[THOUGHTS_ON_COMPANY]
            doc["likes"] = row[LIKES]
            doc["links"] = row[LINKS]
            doc["phone_number"] = row[PHONE]
            if doc.get("status") != "Rejected":
                doc["status"] = "Open"

            if name:
                await client.update(doc)
                print("Updated " + row[EMAIL])
            else:
                await client.insert(doc)
                print("Inserted " + row[EMAIL])


if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(sync())
