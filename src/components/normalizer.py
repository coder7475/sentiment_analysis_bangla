import re
import unicodedata
from typing import Dict, List, Optional

class BanglaUnicodeNormalizer:
    """
    Comprehensive Bangla text normalizer using Unicode standards.
    Handles various inconsistencies while preserving linguistic accuracy.
    """
    
    def __init__(self):
        self._setup_unicode_mappings()
        self._compile_patterns()
    
    def _setup_unicode_mappings(self):
        """Define Unicode character mappings for normalization."""
        
        # Zero-width and invisible characters to remove/replace
        self.invisible_chars = {
            '\u200d': '',      # Zero Width Joiner (ZWJ)
            '\u200c': '',      # Zero Width Non-Joiner (ZWNJ)
            '\u00a0': ' ',     # Non-breaking space → regular space
            '\ufeff': '',      # Byte Order Mark (BOM)
            '\u2060': '',      # Word Joiner
            '\u061c': '',      # Arabic Letter Mark
        }
        
        # Bangla digit mappings (if normalization needed)
        self.digit_mappings = {
            '০': '0', '১': '1', '২': '2', '৩': '3', '৪': '4',
            '৫': '5', '৬': '6', '৭': '7', '৮': '8', '৯': '9'
        }
        
        # Punctuation normalization
        self.punctuation_mappings = {
            '॥': '।',         # Devanagari double danda → single danda
            '‍': '',           # Zero width joiner variants
            '‌': '',           # Zero width non-joiner variants
            '।।': '।',        # Double danda → single
        }
        
        # Vowel sign normalization (careful - these affect pronunciation)
        self.vowel_normalizations = {
            # Composite vowels that can be normalized
            '\u09c7\u09be': '\u09cb',  # ে + া = ো (e + aa = o)
            '\u09c7\u09d7': '\u09cc',  # ে + ৗ = ৌ (e + au-length = au)
        }
        
        # Character variants that should be standardized
        self.character_variants = {
            # Only include mappings you're absolutely certain about
            '\u0995\u09cd\u09b7': '\u0995\u09cd\u09b7',  # ক্ষ normalization
        }
        
        # Common OCR/typing errors (use with caution)
        self.ocr_corrections = {
            # Add only well-established corrections
            'ব়': 'ব',  # Remove nukta from ba if incorrectly added
            'জ়': 'জ',  # Remove nukta from ja if incorrectly added
        }
    
    def _compile_patterns(self):
        """Compile regex patterns for efficient processing."""
        
        # Pattern for duplicate diacritics
        self.duplicate_diacritics = re.compile(r'([ািীুূেৈোৌংঁঃ])\1+')
        
        # Pattern for multiple whitespace
        self.multiple_whitespace = re.compile(r'\s+')
        
        # Pattern for Bangla digits
        self.bangla_digits = re.compile(r'[০-৯]')
        
        # Pattern for ASCII digits
        self.ascii_digits = re.compile(r'[0-9]')
        
        # Pattern for multiple punctuation
        self.multiple_punct = re.compile(r'([।,;:!?])\1+')
        
        # Pattern for hasanta (virama) normalization
        self.hasanta_pattern = re.compile(r'\u09cd(?=\s|$)')
    
    def normalize_unicode(self, text: str, form: str = 'NFC') -> str:
        """
        Apply Unicode normalization.
        
        Args:
            text: Input text
            form: Unicode normalization form ('NFC', 'NFD', 'NFKC', 'NFKD')
        
        Returns:
            Unicode normalized text
        """
        return unicodedata.normalize(form, text)
    
    def remove_invisible_chars(self, text: str) -> str:
        pattern = re.compile('|'.join(map(re.escape, self.invisible_chars.keys())))
        return pattern.sub(lambda m: self.invisible_chars[m.group(0)], text)

    
    def normalize_whitespace(self, text: str) -> str:
        """Normalize whitespace characters."""
        # Replace multiple whitespace with single space
        text = self.multiple_whitespace.sub(' ', text)
        # Strip leading/trailing whitespace
        return text.strip()
    
    def normalize_punctuation(self, text: str) -> str:
        """Normalize punctuation marks."""
        for punct, normalized in self.punctuation_mappings.items():
            text = text.replace(punct, normalized)
        
        # Handle multiple consecutive punctuation
        text = self.multiple_punct.sub(r'\1', text)
        return text
    
    def normalize_vowels(self, text: str) -> str:
        """Normalize vowel combinations and signs."""
        for combination, normalized in self.vowel_normalizations.items():
            text = text.replace(combination, normalized)
        
        # Remove duplicate diacritics
        text = self.duplicate_diacritics.sub(r'\1', text)
        return text
    
    def normalize_digits(self, text: str, to_ascii: bool = False, remove: bool = False) -> str:
        """
        Normalize digit representations.
        
        Args:
            text: Input text
            to_ascii: Convert Bangla digits to ASCII
            remove: Remove all digits
        
        Returns:
            Text with normalized digits
        """
        if remove:
            text = self.bangla_digits.sub('', text)
            text = self.ascii_digits.sub('', text)
        elif to_ascii:
            for bangla, ascii_digit in self.digit_mappings.items():
                text = text.replace(bangla, ascii_digit)
        
        return text
    
    def apply_character_variants(self, text: str) -> str:
        """Apply character variant normalizations."""
        for variant, standard in self.character_variants.items():
            text = text.replace(variant, standard)
        return text
    
    def apply_ocr_corrections(self, text: str) -> str:
        """Apply common OCR error corrections (use with caution)."""
        for error, correction in self.ocr_corrections.items():
            text = text.replace(error, correction)
        return text
    
    def normalize_hasanta(self, text: str) -> str:
        """
        Normalize hasanta (virama) usage.
        Remove trailing hasanta that don't form conjuncts.
        """
        # Remove hasanta at word boundaries or end of text
        text = self.hasanta_pattern.sub('', text)
        return text
    
    def get_unicode_info(self, text: str) -> List[Dict]:
        """
        Get Unicode information for each character in text.
        Useful for debugging normalization issues.
        """
        info = []
        for char in text:
            info.append({
                'char': char,
                'unicode': f'U+{ord(char):04X}',
                'name': unicodedata.name(char, 'UNKNOWN'),
                'category': unicodedata.category(char),
                'combining': unicodedata.combining(char)
            })
        return info
    
    def normalize(self, 
                 text: str, 
                 unicode_form: str = 'NFC',
                 remove_digits: bool = False,
                 digits_to_ascii: bool = False,
                 apply_ocr_fixes: bool = False,
                 normalize_hasanta: bool = True) -> str:
        """
        Comprehensive text normalization.
        
        Args:
            text: Input text to normalize
            unicode_form: Unicode normalization form
            remove_digits: Remove all digits
            digits_to_ascii: Convert Bangla digits to ASCII
            apply_ocr_fixes: Apply OCR error corrections
            normalize_hasanta: Normalize hasanta usage
        
        Returns:
            Normalized text
        """
        
        # Step 1: Unicode normalization
        text = self.normalize_unicode(text, unicode_form)
        
        # Step 2: Remove invisible characters
        text = self.remove_invisible_chars(text)
        
        # Step 3: Normalize whitespace
        text = self.normalize_whitespace(text)
        
        # Step 4: Normalize punctuation
        text = self.normalize_punctuation(text)
        
        # Step 5: Normalize vowels and diacritics
        text = self.normalize_vowels(text)
        
        # Step 6: Handle digits
        text = self.normalize_digits(text, digits_to_ascii, remove_digits)
        
        # Step 7: Apply character variants
        text = self.apply_character_variants(text)
        
        # Step 8: Normalize hasanta (optional)
        if normalize_hasanta:
            text = self.normalize_hasanta(text)
        
        # Step 9: Apply OCR corrections (optional, use with caution)
        if apply_ocr_fixes:
            text = self.apply_ocr_corrections(text)
        
        return text

# Convenience function for quick normalization
def normalize_bangla_text(text: str, **kwargs) -> str:
    """
    Quick normalization function.
    
    Args:
        text: Text to normalize
        **kwargs: Additional options for normalization
    
    Returns:
        Normalized text
    """
    normalizer = BanglaUnicodeNormalizer()
    return normalizer.normalize(text, **kwargs)

# Example usage and testing
if __name__ == "__main__":
    # Initialize normalizer
    normalizer = BanglaUnicodeNormalizer()
    
    # Test cases
    test_cases = [
        "বাংলা   টেক্সট",                    # Multiple whitespace
        "আমার\u200dনাম",                     # With ZWJ
        "বাংলা১২৩text",                      # Mixed digits
        "হেলো।।।",                         # Multiple punctuation
        "কিছু\u00a0টেক্সট",                 # Non-breaking space
        "ে\u09beকার",                       # Composite vowel
        "কিছু\u09cd",                       # Trailing hasanta
        "আমি\u200cআছি",                     # With ZWNJ
    ]
    
    print("=== Bangla Unicode Normalization Examples ===\n")
    
    for i, text in enumerate(test_cases, 1):
        print(f"Test {i}:")
        print(f"Original: '{text}'")
        
        # Show Unicode info for first few characters
        if len(text) <= 10:
            unicode_info = normalizer.get_unicode_info(text)
            print("Unicode info:", [f"{info['char']}({info['unicode']})" for info in unicode_info])
        
        # Basic normalization
        normalized = normalizer.normalize(text)
        print(f"Normalized: '{normalized}'")
        
        # Normalization with digit removal
        no_digits = normalizer.normalize(text, remove_digits=True)
        print(f"No digits: '{no_digits}'")
        
        print("-" * 50)
    
    # Demonstrate different normalization levels
    print("\n=== Different Normalization Levels ===")
    sample_text = "বাংলা\u200d১২৩  টেক্সট।।"
    
    print(f"Original: '{sample_text}'")
    print(f"Basic: '{normalizer.normalize(sample_text)}'")
    print(f"No digits: '{normalizer.normalize(sample_text, remove_digits=True)}'")
    print(f"ASCII digits: '{normalizer.normalize(sample_text, digits_to_ascii=True)}'")
    print(f"With OCR fixes: '{normalizer.normalize(sample_text, apply_ocr_fixes=True)}'")