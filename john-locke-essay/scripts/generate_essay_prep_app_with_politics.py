#!/usr/bin/env python3
"""
Generate Essay Prep App with Politics
Combines all modular parts to create the complete HTML file
"""

import sys
import os

# Add the parts directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'parts'))

from jl_app_part1_head import get_app_head
from jl_app_part2_nav import get_app_nav
from jl_app_part3_dashboard import get_app_dashboard
from jl_app_part4_econ_q1 import get_econ_q1
from jl_app_part5_econ_q2 import get_econ_q2
from jl_app_part6_econ_q3 import get_econ_q3
from jl_app_part7_pol_q1 import get_pol_q1
from jl_app_part8_pol_q2 import get_pol_q2
from jl_app_part9_pol_q3 import get_pol_q3
from jl_app_part10_resources import get_app_resources
from jl_app_part11_footer import get_app_footer

def generate_essay_prep_app():
    """Generate the complete essay prep app HTML"""
    
    # Combine all parts
    html_content = (
        get_app_head() +
        get_app_nav() +
        get_app_dashboard() +
        get_econ_q1() +
        get_econ_q2() +
        get_econ_q3() +
        get_pol_q1() +
        get_pol_q2() +
        get_pol_q3() +
        get_app_resources() +
        get_app_footer()
    )
    
    return html_content

def main():
    """Main function to generate and save the HTML file"""
    
    # Generate the HTML
    html_content = generate_essay_prep_app()
    
    # Determine output path
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_dir, '..', 'outputs')
    output_path = os.path.join(output_dir, 'essay-prep-app.html')
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Write the file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    # Get file size
    file_size = os.path.getsize(output_path)
    
    print(f"Generated: {output_path}")
    print(f"File size: {file_size:,} bytes ({file_size/1024:.1f} KB)")
    print(f"Includes: Economics (3 questions) + Politics (3 questions)")
    print(f"Sections: Dashboard, Timeline, 6 Question Pages, Frameworks, Past Questions, Reading, Mentorship, Checklist")

if __name__ == "__main__":
    main()