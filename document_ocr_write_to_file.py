#!/usr/bin/env python

import sys
import io
import os

def detect_document(path):

    file = open('out.txt','a')

    """Detects document features in an image."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.document_text_detection(image=image)

    for page in response.full_text_annotation.pages:
        for block in page.blocks:
            # file.write('\nBlock confidence: {}\n'.format(block.confidence))

            for paragraph in block.paragraphs:
                # file.write('Paragraph confidence: {}'.format(
                #     paragraph.confidence))

                for word in paragraph.words:
                    word_text = ''.join([
                        symbol.text for symbol in word.symbols
                    ])
                    file.write('{} '.format(
                        word_text))

                    # for symbol in word.symbols:
                    #     file.write('\tSymbol: {} (confidence: {})'.format(
                    #         symbol.text, symbol.confidence))
                file.write('\n')
    file.write('-----------\n')
    file.close()

detect_document(sys.argv[1])
