  <h1>PDF Splitter</h1>

  <h2>Features</h2>
    <ul>
        <li><strong>General PDF Splitting:</strong> Split any multi-page PDF into individual pages.</li>
        <li><strong>Custom Naming Convention:</strong> Each split page is saved as "Page {page_number}.pdf".</li>
        <li><strong>Interactive Interface:</strong> Prompt-based selection of source PDF and output directory.</li>
        <li><strong>Progress Indicator:</strong> Visual progress bar to monitor the splitting process.</li>
        <li><strong>Error Handling:</strong> Graceful handling of common errors with informative messages.</li>
    </ul>

  <h2>Prerequisites</h2>
    <ul>
        <li><strong>Python 3.6 or higher:</strong> Ensure Python is installed on your system. Download it from the <a href="https://www.python.org/downloads/">official Python website</a>.</li>
    </ul>

  <h2>Installation</h2>
    <ol>
        <li><strong>Clone the Repository</strong>
            <pre><code>git clone https://github.com/robertjbass/pdf-splitter.git
cd pdf-splitter</code></pre>

</li>
<li><strong>Set Up a Virtual Environment (Recommended)</strong>
<pre><code>python3 -m venv venv
</code></pre>
</li>
<li><strong>Activate the Virtual Environment</strong>
<ul>
<li><strong>macOS/Linux:</strong>
<pre><code>source venv/bin/activate
</code></pre>
</li>
<li><strong>Windows:</strong>
<pre><code>venv\Scripts\activate
</code></pre>
</li>
</ul>
<em>After activation, your terminal prompt should be prefixed with <code>(venv)</code>.</em>
</li>
<li><strong>Install Required Python Libraries</strong>
<pre><code>pip install -r requirements.txt
</code></pre>
<em>If <code>requirements.txt</code> is not present, install directly:</em>
<pre><code>pip install PyPDF2 tqdm
</code></pre>
</li>
<li><strong>Prepare the Source Directory</strong>
<pre><code>mkdir source
</code></pre>
<em>Place your PDF files inside the <code>source/</code> directory.</em>
</li>
</ol>

  <h2>Usage</h2>
    <ol>
        <li><strong>Ensure the Virtual Environment is Activated</strong>
            <em>If not already activated, activate it:</em>
            <ul>
                <li><strong>macOS/Linux:</strong>
                    <pre><code>source venv/bin/activate</code></pre>
                </li>
                <li><strong>Windows:</strong>
                    <pre><code>venv\Scripts\activate</code></pre>
                </li>
            </ul>
        </li>
        <li><strong>Run the PDF Splitter Script</strong>
            <pre><code>python main.py</code></pre>
        </li>
        <li><strong>Follow the Interactive Prompts</strong>
            <ul>
                <li><strong>Select the PDF to Split:</strong>
                    <p>The script will display a list of available PDF files in the <code>source</code> directory. Enter the number corresponding to the PDF you wish to split.</p>
                    <pre><code>=== PDF Splitter ===

Available PDF files:

1.  example.pdf
2.  another_document.pdf
    Enter the number of the PDF file you want to split (1-2): 1
    Selected file: 'example.pdf'
    </code></pre>
    </li>
    <li><strong>Specify the Output Directory:</strong>
    <p>Enter the name of the output directory where the split pages will be saved. Press <strong>Enter</strong> to use the default <code>output</code> directory.</p>
    <pre><code>Enter the name of the output directory (default: 'output'):
    </code></pre>
    </li>
    </ul>
    </li>
    <li><strong>Monitor the Splitting Process</strong>
    <p>The script will display a progress bar and save each split page with the filename "Page {page_number}.pdf" in the specified output directory.</p>
    <pre><code>Created output directory at 'output'.
    Total pages to split: 10
    Splitting Pages: 100%|██████████| 10/10 [00:02<00:00, 4.85it/s]
    Saved: Page 1.pdf
    Saved: Page 2.pdf
    ...
    Saved: Page 10.pdf
    PDF splitting completed successfully.
    </code></pre>
    </li>
    <li><strong>Verify the Output</strong>
    <p>Navigate to the <code>output</code> directory to find your split PDF files.</p>
    <pre><code>cd output
    ls
    </code></pre>
    <p>Example Output:</p>
    <pre><code>Page 1.pdf
    Page 2.pdf
    ...
    Page 10.pdf</code>
    </pre>
    </li>
    </ol>

    <h2>Project Structure</h2>
    <pre><code>pdf-splitter/
    │
    ├── output/ # Folder where individual PDFs will be saved
    ├── source/ # Folder containing the source PDFs
    │ └── example.pdf # Your source PDF files
    ├── main.py # The Python script
    ├── requirements.txt # Python dependencies
    └── venv/ # Virtual environment folder</code></pre>

      <h2>Troubleshooting</h2>
        <ul>
            <li><strong>No PDF Files Found in <code>source/</code> Directory</strong>
                <p><em>Cause:</em> The <code>source</code> directory is empty or does not contain any <code>.pdf</code> files.</p>
                <p><em>Solution:</em> Ensure that your PDF files are placed inside the <code>source</code> folder and have a <code>.pdf</code> extension.</p>
            </li>
            <li><strong>Invalid PDF File</strong>
                <p><em>Cause:</em> The selected file is not a valid PDF or is corrupted.</p>
                <p><em>Solution:</em> Verify the integrity of the PDF file by opening it with a PDF reader to ensure it's not corrupted.</p>
            </li>
            <li><strong>Permission Errors</strong>
                <p><em>Cause:</em> Lack of read/write permissions for the <code>source</code> or <code>output</code> directories.</p>
                <p><em>Solution:</em> Ensure that you have the necessary permissions to read files from the <code>source</code> folder and write to the <code>output</code> folder.</p>
            </li>
            <li><strong>Missing Dependencies</strong>
                <p><em>Cause:</em> Required Python libraries are not installed.</p>
                <p><em>Solution:</em></p>
                <ol>
                    <li>Activate your virtual environment:</li>
                    <pre><code>source venv/bin/activate  # macOS/Linux# venv\Scripts\activate # Windows</code></pre>
    <li>Install dependencies:</li>
    <pre><code>pip install -r requirements.txt
    </code></pre>
    </ol>
    </li>
    <li><strong>Script Not Found or Not Executable</strong>
    <p><em>Cause:</em> The terminal is not in the correct directory.</p>
    <p><em>Solution:</em> Navigate to the project directory containing <code>main.py</code> before running the script.</p>
    <pre><code>cd /path/to/your/pdf-splitter/
    </code></pre>
    </li>
    <li><strong>Virtual Environment Not Activated</strong>
    <p><em>Cause:</em> Dependencies are installed in the virtual environment, but it's not activated.</p>
    <p><em>Solution:</em> Activate the virtual environment:</p>
    <pre><code>source venv/bin/activate # macOS/Linux # venv\Scripts\activate # Windows</code></pre>
    </li>
    </ul>

    <h2>License</h2>
    <p>This project is licensed under the <a href="LICENSE">MIT License</a>.</p>
