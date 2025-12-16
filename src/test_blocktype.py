import unittest

from blocktype import block_to_block_type, BlockType

class TestBlockType(unittest.TestCase):

    def test_code_block(self):
        md = "```CODE IN HERE```"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.CODE)
    
    def test_header_one_block(self):
        md = "# Headers"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_header_two_block(self):
        md = "## Headers"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_header_three_block(self):
        md = "### Headers"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_header_four_block(self):
        md = "#### Headers"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_header_five_block(self):
        md = "##### Headers"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_header_six_block(self):
        md = "###### Headers"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_header_seven_block(self):
        md = "####### Headers"
        block_type = block_to_block_type(md)
        self.assertNotEqual(block_type, BlockType.HEADING)

    def test_quote_single_line_block(self):
        md = ">This is a block of text!"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.QUOTE)

    def test_quote_multi_line_block(self):
        md = ">This is a block of text!\n>This is a block of text!\n>This is a block of text!"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.QUOTE)

    def test_unordered_single_line_block(self):
        md = "- This is a block of text!"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)

    def test_unordered_multi_line_block(self):
        md = "- This is a block of text!\n- This is a block of text!\n- This is a block of text!"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)

    def test_ordered_single_line_block(self):
        md = "1. This is a block of text!"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)

    def test_ordered_multi_line_block(self):
        md = "1. This is a block of text!\n2. This is a block of text!\n3. This is a block of text!"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)

    def test_paragraph_block(self):
        md = "This is a block of text!"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.PARAGRAPH)



if __name__ == "__main__":
    unittest.main()
