import PyPDF2
import os

def delete_duplicate_slides(pdf_path):
    try:
        # Split the file path into directory path, base filename, and extension
        directory, filename = os.path.split(pdf_path)
        base_name, extension = os.path.splitext(filename)
        # Modify the base filename
        outputFilePath = os.path.join("./temp/" + "modified_" + base_name + extension)     

        with open(("./temp/"+filename), 'rb') as file: #the file was saved in the temp folder when uploaded
            reader = PyPDF2.PdfReader(file)
            writer = PyPDF2.PdfWriter()

            num_slides = len(reader.pages)

            for i in range(num_slides):
                # If it's the last slide, add it directly to the output
                if i == num_slides - 1:
                    writer.add_page(reader.pages[i])
                else:
                    current_page = reader.pages[i]
                    next_page = reader.pages[i + 1]

                    #extract the text from the current and next page
                    current_text = current_page.extract_text()
                    next_text = next_page.extract_text()

                    current_words = set(current_text.split())
                    next_words = set(next_text.split())

                    intersection_count = len(current_words.intersection(next_words))
                    union_count = len(current_words.union(next_words))

                    # If at least 85% of the words in the current slide are contained in the next slide, skip the current slide
                    if intersection_count / union_count < 0.85:
                        writer.add_page(current_page)

            with open(outputFilePath, "wb") as output_file:
                writer.write(output_file)

            return outputFilePath

    except Exception as e:
        print(f"An error occurred: {e}")

################################################## The extra ordinary work of a genius Sushil ##########################################
################################################## Copyright Protected @c 12/02/2024 ###################################################
############################## Spent tooo much time on this instead of being productive; so do provide refrence when sharing ###########