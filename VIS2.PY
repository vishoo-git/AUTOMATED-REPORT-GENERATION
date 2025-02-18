import pandas as pd
from fpdf import FPDF
import matplotlib.pyplot as plt

# Step 1: Read data from a file (CSV in this case)
def read_data(file_path):
    data = pd.read_csv(file_path)  # Read CSV file into a DataFrame
    return data

# Step 2: Analyze data (basic analysis like calculating the mean and sum)
def analyze_data(data):
    summary = {}
    summary['mean'] = data.mean()  # Get mean of each column
    summary['sum'] = data.sum()    # Get sum of each column
    summary['describe'] = data.describe()  # Get a detailed statistical summary
    return summary

# Step 3: Create a PDF report
def generate_pdf_report(data_summary, file_path):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Title
    pdf.set_font("Arial", size=16, style='B')
    pdf.cell(200, 10, txt="Data Analysis Report", ln=True, align="C")
    pdf.ln(10)

    # Add general summary
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Data Summary:", ln=True)
    pdf.ln(5)
    pdf.multi_cell(0, 10, txt=str(data_summary['describe']))

    # Add the mean of the data
    pdf.ln(10)
    pdf.cell(200, 10, txt="Mean of the Data:", ln=True)
    pdf.ln(5)
    pdf.multi_cell(0, 10, txt=str(data_summary['mean']))

    # Add the sum of the data
    pdf.ln(10)
    pdf.cell(200, 10, txt="Sum of the Data:", ln=True)
    pdf.ln(5)
    pdf.multi_cell(0, 10, txt=str(data_summary['sum']))

    # Step 4: Optional - Add a plot to the PDF (e.g., histogram)
    pdf.ln(10)
    pdf.cell(200, 10, txt="Data Distribution (Histogram):", ln=True)
    plot_data(data)

    # Save the PDF
    pdf.output(file_path)
    print(f"PDF report saved to {file_path}")

# Function to generate a histogram plot and save it as an image
def plot_data(data):
    # Create a histogram for each numeric column in the dataset
    for column in data.select_dtypes(include='number').columns:
        plt.figure(figsize=(6, 4))
        plt.hist(data[column], bins=10, color='skyblue', edgecolor='black')
        plt.title(f"Histogram of {column}")
        plt.xlabel(column)
        plt.ylabel('Frequency')
        # Save the plot as an image
        plt.savefig(f"{column}_histogram.png")
        plt.close()

        # Add the plot image to the PDF
        pdf.image(f"{column}_histogram.png", x=10, y=pdf.get_y(), w=180)
        pdf.ln(60)  # Leave space for the image

# Main function
def main():
    input_file = 'data.csv'  # Path to your input data file (CSV)
    output_pdf = 'report.pdf'  # Path where the PDF report will be saved

    # Read data
    data = read_data(input_file)
    print("Data loaded successfully.")

    # Analyze data
    summary = analyze_data(data)
    print("Data analysis complete.")

    # Generate PDF report
    generate_pdf_report(summary, output_pdf)

if __name__ == "__main__":
    main()
