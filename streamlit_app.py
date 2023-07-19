import streamlit as st
import json

 

def add_inbound_option(option_index_in):
    col1, col2 = st.columns(2)
    option_name_in = col1.text_input(f"Inbound Option Name {option_index_in}", key=f"name_in_{option_index_in}")
    option_mapping_in = col2.text_input(f"Inbound Option Mapping {option_index_in}", key=f"mapping_in_{option_index_in}")
    return option_name_in, option_mapping_in

 


def add_outbound_option(option_index_out):
    col1, col2 = st.columns(2)
    option_name_out = col1.text_input(f"Outbound Option Name {option_index_out}", key=f"name_out_{option_index_out}")
    option_mapping_out = col2.text_input(f"Outbound Option Mapping {option_index_out}", key=f"mapping_out_{option_index_out}")
    return option_name_out, option_mapping_out

 


def main():
    st.title("Data Source Configuration")

 

    # Data_Source section
    dataSourceName = st.text_input("Data Source Name")
    dataSourcePath = st.text_input("Data Source Path")
    datasourceJoinType = st.text_input("Data Source Join Type")
    datasourceType = st.text_input("Data Source Type")
    dataSourcetargetPath = st.text_input("Data Source Target Path")
    dataSourcePartitionColumn = st.text_input("Data Source Partition Column")
    dateOfBirthFormat = st.text_input("Date of Birth Format")

 

    # Inbound Standardization Columns section
    st.header("Inbound Standardization Columns")
    inbound_options = []
    while True:
        option_name_in, option_mapping_in = add_inbound_option(len(inbound_options) + 1)
        if not option_name_in.strip() and not option_mapping_in.strip():
            break
        inbound_options.append({option_name_in: option_mapping_in})

 

    # Outbound Standardization Columns section
    st.header("Outbound Standardization Columns")
    outbound_options = []
    while True:
        option_name_out, option_mapping_out = add_outbound_option(len(outbound_options) + 1)
        if not option_name_out.strip() and not option_mapping_out.strip():
            break
        outbound_options.append({option_name_out: option_mapping_out})

 

    # Generate Output
    if st.button("Generate Output"):
        inbound_standardization_columns = {}
        for mapping in inbound_options:
            for key, value in mapping.items():
                if key.strip() and value.strip():
                    inbound_standardization_columns[key] = value

 

        outbound_standardization_columns = {}
        for mapping in outbound_options:
            for key, value in mapping.items():
                if key.strip() and value.strip():
                    outbound_standardization_columns[key] = value

 

        additional_lists = {
            "contactedList": {
                "sourcePath": "adhoc/contacted_list/",
                "firstName": "FirstName",
                "lastName": "LastName",
                "fullName": "FullName",
                "cdate": "ContactDate",
                "day": "day"
            },
            "blackList": {
                "sourcePath": "adhoc/blacklist/",
                "firstName": "FirstName",
                "lastName": "LastName",
                "fullName": "FullName",
                "national_id": "NationalId"
            },
            "dncList": {
                "sourcePath": "adhoc/do_not_call_list/",
                "firstName": "first_name",
                "lastName": "last_name",
                "fullName": "FullName",
                "mobileNo": "phone_no"
            },
            "mobilecodeList": {
                "sourcePath": "adhoc/mobilecodes/",
                "mobileCode": "MobileCode"
            }
        }

 

        data = {
            "Data_Source": {
                "dataSourceName": dataSourceName,
                "datasourcePath": dataSourcePath,
                "datasourceJoinType": datasourceJoinType,
                "datasourceType": datasourceType,
                "dataSourcetargetPath": dataSourcetargetPath,
                "dataSourcePartitionColumn": dataSourcePartitionColumn,
                "dateOfBirthFormat": dateOfBirthFormat
            },
            "inboundStandardizationColumns": inbound_standardization_columns,
            "outboundStandardizationColumns": outbound_standardization_columns,
            **additional_lists
        }


        st.text_area("Output", value=json.dumps(data, indent=2), height=800)
        st.success("Done")

 

if __name__ == "__main__":
    main()
